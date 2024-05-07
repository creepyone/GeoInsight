<template>
    <div v-if="show" class="modal-shadow" @click.self="closeModal">
        <div class="modal">
            <div class="modal-close" @click="closeModal">&#10006;</div>
            <slot name="title">
                <h5 class="modal-title">Какой-то текст</h5>
            </slot>
            <slot name="body">
                <div class="modal-content">
                    Какой-то контент
                </div>
            </slot>
        </div>
    </div>
</template>
 
<script>
    export default {
        name: "ModalWindow",
        data: function () {
            return {
                show: false
            }
        },
        methods: {
            closeModal: function () {
                this.show = false
            }
        },
        props: {
            request_id: {
                type: String
            }
        }
    }
</script>
 
<style scoped>
    .modal-shadow {
        position: absolute;
        top: 0;
        left: 0;
        min-height: 100%;
        width: 100%;
        background: rgba(0, 0, 0, 0.39);
    }
 
    .modal {
    background: #FFFFFF;
    border-radius: 8px;
    padding: 15px;
    max-width: 500px;
    max-height: 300px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    }

    .modal-close {
    text-align: right;
    }
    .modal-close:hover {
    cursor: pointer;
    }
    .modal-title {
    text-align: center;
    }
    
</style>