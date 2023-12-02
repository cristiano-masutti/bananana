<template>
    <div style="background-color: #242424; height: 75vh; overflow-y: auto;">
      <div class="album-container">
        <AlbumRecord />
        <AlbumRecord />
        <AlbumRecord />
        <AlbumRecord />
      </div>
    </div>
  </template>
  
  <script>
  import AlbumRecord from './AlbumRecord.vue'
  import axios from 'axios'
  
  export default {
    name: 'SharkVue',
    components: {
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
        try {
          const response = await axios.get(path);
          console.log(response.data);
          this.msg = response.data;
        } catch (error) {
          console.log("Error:", error);
        }
      },
    }
  }
  </script>
  
  <style scoped>
  .album-container {
    display: flex;
    flex-wrap: wrap;
    justify-content:space-around;
  }
  
  /* Adjust the width of AlbumRecord components as needed */
  .album-container AlbumRecord {
    width: 48%; /* Adjust the width as per your layout */
    margin-bottom: 10px; /* Add margin for spacing between elements */
  }
  </style>
  