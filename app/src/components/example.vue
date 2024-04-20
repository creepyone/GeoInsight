<script>
import { saveAs } from 'file-saver';
export default {
  methods: {
    action() {
      if (document.getElementById('btn-process').style.visibility == 'hidden') {
        document.getElementById('btn-process').style.visibility = 'visible';
      } else {
        document.getElementById('btn-process').style.visibility = 'hidden';
      }
      map.click();
    },
  },
  mounted() {
    var map = L.map(this.$refs['mapElement'], {
      zoomControl: true,
      maxZoom: 18,
      minZoom: 15,
    }).fitBounds([
      [55.635207589609905, 37.64153644777789],
      [55.63828100193793, 37.66559566363489],
    ]);
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
    map.createPane('pane_OSMStandard_1');
    map.getPane('pane_OSMStandard_1').style.zIndex = 401;
    var layer_OSMStandard_1 = L.tileLayer(
      'http://tile.openstreetmap.org/{z}/{x}/{y}.png',
      {
        pane: 'pane_OSMStandard_1',
        opacity: 1.0,
        attribution:
          '<a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors, CC-BY-SA</a>',
        minZoom: 15,
        maxZoom: 28,
        minNativeZoom: 0,
        maxNativeZoom: 19,
      }
    );
    layer_OSMStandard_1;
    map.addLayer(layer_OSMStandard_1);
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
    L.control
      .layers(
        baseMaps,
        {
          'OSM Standard': layer_OSMStandard_1,
          'Google Satellite': layer_GoogleSatellite_0,
        },
        { collapsed: false }
      )
      .addTo(map);
    setBounds();

    map.on('moveend', function () {
      console.log('moving:', map.getBounds());
    });

    map.on('dragend', function onDragEnd() {
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
      var coord = e.latlng.toString().split(',');
      var lat = coord[0].split('(');
      var lng = coord[1].split(')');
      console.log(
        'You clicked the map at latitude: ' +
          lat[1] +
          ' and longitude:' +
          lng[0]
      );
      var snapshot = document.getElementById('snapshot');
      leafletImage(map, function (err, canvas) {
        // now you have canvas
        // example thing to do with that canvas:
        var img = document.createElement('img');
        var dimensions = map.getSize();
        img.width = dimensions.x;
        img.height = dimensions.y;
        img.src = canvas.toDataURL();

        canvas.toBlob(function (blob) {
          saveAs(blob, 'pretty image.png');
        });
      });
    });
  },
};
</script>

<template>
  <container>
    <h4>Анализ поверхности с помощью компьютерного зрения</h4>

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
            value=""
            checked
          />
          <small class="d-block text-body-secondary">Вода</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            value=""
          />
          <small class="d-block text-body-secondary">Деревья</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            value=""
          />
          <small class="d-block text-body-secondary">Застройка</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            value=""
          />
          <small class="d-block text-body-secondary">Поля</small>
        </label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            value=""
          />
          <small class="d-block text-body-secondary">Дороги</small>
        </label>

        <label class="list-group-item d-flex gap-2">Детекция строений</label>

        <label class="list-group-item d-flex gap-2">
          <input
            class="form-check-input flex-shrink-0"
            type="checkbox"
            value=""
          />
          <small class="d-block text-body-secondary">Включить детекцию</small>
        </label>
        <button
          class="btn btn-primary"
          id="btn-analyze"
          type="button"
          @click="action()"
          style="position: relative; top: 80px; left: 0px"
        >
          <span role="status">Проанализировать</span>
        </button>

        <button
          class="btn btn-primary"
          id="btn-process"
          type="button"
          style="visibility: hidden"
          disabled
        >
          <span
            class="spinner-border spinner-border-sm"
            aria-hidden="true"
          ></span>
          <span role="status"> Loading...</span>
        </button>
      </div>
    </div>
    <div id="snapshot"></div>
  </container>
</template>
