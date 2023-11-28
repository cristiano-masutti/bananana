<template>
    <div style="background-color: blueviolet;height: 100%; widht:100%; overflow: auto;">
        <h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1><h1>Pippo</h1>

    </div>
</template>

<script>


import axios from 'axios'
export default {
    name: 'SharkVue',
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