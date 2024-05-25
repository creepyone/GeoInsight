<script>
import axios from "axios";
export default {
  data() {
    return {
      minimap: null,
      placeholderMap: null,
      placeholderLayerControl: null,
      pkk: []
    };
  },
  methods: {
    addPKK() {
      var mapp = this.placeholderMap[0];
      var btn_PKK = document.getElementById("btn-pkk");
      var btn_analyze = document.getElementById("btn-analyze");

      if (btn_PKK.textContent == "Добавить кадастровую карту")
      {
        mapp.createPane('pane_pkk_rosreestr_1');
        mapp.getPane('pane_pkk_rosreestr_1').style.zIndex = 800;
        var layer_pkk_rosreestr_1 = L.tileLayer('https://gext.ru/rosreestr_xyz/{z}/{x}/{y}.png', {
          pane: 'pane_pkk_rosreestr_1',
          opacity: 1.0,
          attribution: '',
          maxZoom: 18,
          minZoom: 15,
          minNativeZoom: 0,
          maxNativeZoom: 20,
        });
        mapp.addLayer(layer_pkk_rosreestr_1);
        btn_PKK.textContent = "Скрыть кадастровую карту";
        btn_analyze.disabled = true;
        this.placeholderMap[0] = mapp;
        this.pkk.push(layer_pkk_rosreestr_1);
      }
      else
      {
        console.log(this.pkk[0]);
        console.log(mapp.hasLayer(this.pkk[0]));
        mapp.removeLayer(this.pkk.pop());
        btn_PKK.textContent = "Добавить кадастровую карту";
        btn_analyze.disabled = false;
        this.placeholderMap[0] = mapp;
      }

    },
    action() {
      var mapp = this.placeholderMap[0];
      var layy = this.placeholderLayerControl[0];
      var coordinates = mapp.getBounds();

      leafletImage(this.minimap, function (err, canvas) {
          var image_data = canvas.getContext('2d').getImageData(0, 0, canvas.width, canvas.height);
          var flags = {
            'Water': document.getElementById("water").checked
            , 'Trees': document.getElementById("trees").checked
            , 'Building': document.getElementById("buildings").checked
            , 'Agriculture': document.getElementById("fields").checked
            , 'Road': document.getElementById("roads").checked
            , 'buildings_detection': document.getElementById("buildings_detection").checked
          }
          axios.post(
            'http://127.0.0.1:5000/model_api/get_prediction'
            , {
              image: image_data.data
              , width: image_data.width
              , height: image_data.height
              , ml_task_flags: flags
              , user_id: parseInt(window.location.pathname.split('/')[2])
            }
            )
            .then(response => {
              console.log(response)
              const current = new Date();
              //const date = current.getDate()+'/'+(current.getMonth()+1)+'/'+current.getFullYear();
              const time = current.getHours() + ":" + current.getMinutes() + ":" + current.getSeconds();
              //const dateTime = date +' '+ time;

              var northEast = [coordinates.getSouthWest().lat, coordinates.getSouthWest().lng];
              var southWest = [coordinates.getNorthEast().lat, coordinates.getNorthEast().lng];
              coordinates = [southWest, northEast];

              var imageSegmentation = L.imageOverlay(response.data['path_segmentation'], coordinates);
              layy.addOverlay(imageSegmentation, "Классификация от " + time); 
              
              console.log(response.data['path_detection'])
              if (response.data['path_detection'] != null){
                var imageDetection = L.imageOverlay(response.data['path_detection'], coordinates);
                layy.addOverlay(imageDetection, "Детекция от " + time);
              }

              
              console.log(response.status)
            }).catch((e) => {
              alert('Model server is not responding!')
            });
      })
    },
  },
  mounted() {
    this.placeholderMap = [];
    this.placeholderLayerControl = [];

    var map = L.map(this.$refs['mapElement'], {
      zoomControl: true,
      maxZoom: 18,
      minZoom: 15,
    }).fitBounds([
      [55.635207589609905, 37.64153644777789],
      [55.63828100193793, 37.66559566363489],
    ]);
    this.placeholderMap.push(map);
    var hash = new L.Hash(map);
    map.attributionControl.setPrefix(
      '<a href="https://github.com/tomchadwin/qgis2web" target="_blank">qgis2web</a> &middot; <a href="https://leafletjs.com" title="A JS library for interactive maps">Leaflet</a> &middot; <a href="https://qgis.org">QGIS</a>'
    );
    var autolinker = new Autolinker({
      truncate: { length: 30, location: 'smart' },
    });
    function removeEmptyRowsFromPopupContent(content, feature) {
      var tempDiv = document.createElement('div');
      tempDiv.innerHTML = content;
      var rows = tempDiv.querySelectorAll('tr');
      for (var i = 0; i < rows.length; i++) {
        var td = rows[i].querySelector('td.visible-with-data');
        var key = td ? td.id : '';
        if (
          td &&
          td.classList.contains('visible-with-data') &&
          feature.properties[key] == null
        ) {
          rows[i].parentNode.removeChild(rows[i]);
        }
      }
      return tempDiv.innerHTML;
    }
    document.querySelector('.leaflet-popup-pane').addEventListener(
      'load',
      function (event) {
        var tagName = event.target.tagName,
          popup = map._popup;
        // Also check if flag is already set.
        if (tagName === 'IMG' && popup && !popup._updated) {
          popup._updated = true; // Set flag to prevent looping.
          popup.update();
        }
      },
      true
    );
    var bounds_group = new L.featureGroup([]);
    function setBounds() {}
    map.createPane('pane_GoogleSatellite_0');
    map.getPane('pane_GoogleSatellite_0').style.zIndex = 400;
    var layer_GoogleSatellite_0 = L.tileLayer(
      'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
      {
        pane: 'pane_GoogleSatellite_0',
        opacity: 1.0,
        attribution:
          '<a href="https://www.google.at/permissions/geoguidelines/attr-guide.html">Map data ©2015 Google</a>',
        minZoom: 15,
        maxZoom: 28,
        minNativeZoom: 0,
        maxNativeZoom: 20,
      }
    );
    layer_GoogleSatellite_0;
    map.addLayer(layer_GoogleSatellite_0);

    var osmGeocoder = new L.Control.Geocoder({
      collapsed: true,
      position: 'topleft',
      text: 'Search',
      title: 'Testing',
    }).addTo(map);
    document.getElementsByClassName(
      'leaflet-control-geocoder-icon'
    )[0].className += ' fa fa-search';
    document.getElementsByClassName('leaflet-control-geocoder-icon')[0].title +=
      'Search for a place';
    var baseMaps = {};
    var layerControl =L.control
      .layers(
        baseMaps,
        {
          
        },
        { collapsed: false }
      )
      .addTo(map);
    this.placeholderLayerControl.push(layerControl);
      setBounds();
    this.minimap = map;

    map.on('moveend', function () {
      this.minimap = map;
      //console.log('moving:', map.getBounds());
    });

    map.on('dragend', function onDragEnd() {
      this.minimap = map;
      var width = map.getBounds().getEast() - map.getBounds().getWest();
      var height = map.getBounds().getNorth() - map.getBounds().getSouth();

      console.log(
        'center:' +
          map.getCenter() +
          '\n' +
          'width:' +
          width +
          '\n' +
          'height:' +
          height +
          '\n' +
          'size in pixels:' +
          map.getSize()
      );
    });

    map.on('click', function (e) {
      this.minimap = map;
      var coord = e.latlng.toString().split(',');
      var lat = coord[0].split('(');
      var lng = coord[1].split(')');
      console.log(
        'You clicked the map at latitude: ' +
          lat[1] +
          ' and longitude:' +
          lng[0]
      );
    });
  },
};
</script>

<template>
  <container>
    <h4 class="display-8 fw-normal" align="center">
      Анализ поверхности с помощью компьютерного зрения
    </h4>

    <div class="d-flex p-2 bd-highlight">
      Выберите область для анализа на карте:
    </div>

    <div class="d-flex flex-column flex-md-row">
      <div
        class="container"
        style="
          width: 900px;
          height: 900px;
          position: relative;
          top: 0px;
          left: -10px;
          background: #e0f1ef;
          border-radius: 20px;
        "
      >
        <div
          id="map"
          ref="mapElement"
          style="
            top: 15px;
            left: 2px;
            width: 870px;
            height: 870px;
            border: 3px solid #888;
          "
        ></div>
      </div>

      <div class="list-group d-inline-flex" style="position: relative">
        <label class="list-group-item d-flex gap-2"
          >Классификация поверхностей</label
        >
        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            id="water"
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Вода</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            id="trees"
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Деревья</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            id="buildings"
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Застройка</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            id="fields"
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Поля</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            id="roads"
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Дороги</small>
        </label>

        <label class="list-group-item d-flex gap-2">Детекция строений</label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            id="buildings_detection"
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Включить детекцию</small>
        </label>
        <button
          class="btn btn-primary"
          id="btn-analyze"
          type="button"
          @click="action()"
          style="position: relative; top: 20px; left: 0px"
        >
          <span role="status">Проанализировать</span>
        </button>

        <button
          class="btn btn-primary"
          id="btn-pkk"
          type="button"
          @click="addPKK()"
          style="position: relative; top: 40px; left: 0px"
        >
          <span role="status">Добавить кадастровую карту</span>
        </button>
      </div>
    </div>
    <hr>
  </container>
</template>