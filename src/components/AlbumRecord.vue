<template>
    <div class="album-record">
        <div class="top">
            <div class="image-container">
                <img src="https://f4.bcbits.com/img/0012716886_2.jpg" alt="Album Cover" height="100" width="100"/>
              </div>
              <div class="info-container">
                  <h4>Artist Name</h4>
                  <h4>Album Name</h4>
              </div>
        </div>
        <div class="description">
            Description
        </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AlbumRecord",
  };
  </script>
  
  <style scoped>
  .album-record {
    display: flex;
    flex-direction: column;
    height: 200px;
    width: 500px;
    margin: 10px;
    background-color: #D9D9D9;
    border-radius: 1%;
  }

  .top {
    display: flex;
    flex-direction: row;
    height: 55%;
  }
  
  .image-container {
    margin: 10px;
  }
  
  .info-container {
    flex: 1;

  }
  
  .description {
    height: 45%;
    margin-left: 10px;
    margin-top: 5px;
  }
  </style>
  