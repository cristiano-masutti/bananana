<template>
  <div class="album-record">
    <div class="top">
      <div class="image-container">
        <!-- Use v-if to check if result has an image property, and display the image if available -->
        <img v-if="result.image" :src="result.image" alt="Album Cover" height="100" width="100" />
      </div>
      <div class="info-container">
        <!-- Display artist and album names from the result prop -->
        <h4>{{ result.artist }}</h4>
        <h4>{{ result.album }}</h4>
      </div>
    </div>
    <div class="description">
      {{ result.description }}
    </div>
  </div>
</template>

<script>
export default {
  name: "AlbumRecord",
  props: {
    result: Object,
  },
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
