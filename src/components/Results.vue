<template>
    <div style="background-color: #242424; height: 75vh; overflow-y: auto;">
        <AlbumRecord/>
    </div>
</template>

<script>

import AlbumRecord from './AlbumRecord.vue'
import axios from 'axios'
export default {
    name: 'SharkVue',
    components : {
        AlbumRecord
    },
    data() {
        return {
            msg: ""
        }
    },
    async mounted() {
        console.log('Component mounted.')
        this.getResponse();
    },
    methods: {
        async getResponse() {
            console.log('Getting response from server.')
            const path = 'http://127.0.0.1:5000/shark';
            await axios.get(path)
                .then((response) => {
                    console.log(response.data);
                    this.msg = response.data;
                })
                .catch(error => {
                    console.log("err", error);
                })
        },
    }

}

</script>

<style>
    
</style>