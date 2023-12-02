<template>
    <div style="background-color: #D9D9D9; margin-top: 10px; margin-right: 50px; margin-bottom: 30px; height: 70vh; overflow-y: auto;">
        <h1 style="margin-left: 10px">History</h1>
        
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