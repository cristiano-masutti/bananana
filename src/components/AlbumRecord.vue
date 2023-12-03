<template>
  <a :href="result.Link" class="album-record linkref">
    <div class="top">
      <div class="image-container">
        <img v-if="result.Img" :src="result.Img" alt="Album Cover" class="album-cover" />
      </div>
      <div class="info-container">
        <h4 class="artist">{{ result.Artist }}</h4>
        <h4 class="album">{{ result.Album }}</h4>
      </div>
    </div>
    <div class="description">
      <p class="description-text">{{ truncateDescription(result.Description, 22) }}</p>
    </div>
  </a>
</template>

<script>
export default {
  name: "AlbumRecord",
  props: {
    result: Object,
  },
  methods: {
    truncateDescription(description, maxWords) {
      const words = description.split(' ');
      if (words.length <= maxWords) {
        return description; // If the number of words is less than or equal to the limit, return the original description
      }
      const truncated = words.slice(0, maxWords).join(' ') + '...';
      return truncated;
    },
  },
};
</script>

<style scoped>
.linkref {
  text-decoration: none;
  color: inherit;
  outline: none;
  transition: background-color 0.3s ease;
}

.linkref:hover {
  background-color: #F0F0F0; /* Change background color on hover */
}

.album-record {
  display: flex;
  flex-direction: column;
  height: auto;
  max-width: 500px; 
  min-width: 500px ;/* Set a maximum width for responsiveness */
  margin: 10px;
  background-color: #D9D9D9;
  border-radius: 8px;
  overflow: hidden; /* Hide overflow content */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
}

.top {
  display: flex;
  flex-direction: row;
  height: 55%;
  overflow: hidden; /* Hide overflow content */
}

.image-container {
  margin: 10px;
  overflow: hidden; /* Hide overflow content */
}

.album-cover {
  width: 100px; /* Set a fixed width for the album cover */
  height: 100px; /* Set a fixed height for the album cover */
  object-fit: cover; /* Maintain aspect ratio and cover the container */
  border-radius: 4px;
}

.info-container {
  flex: 1;
  padding: 10px; /* Add padding for better spacing */
}

.artist, .album {
  margin: 0; /* Remove default margin for the headers */
  font-size: 16px; /* Adjust font size */
}

.description {
  flex: 1;
  margin: 10px;
  margin-top: 5px;
  margin-bottom: 10px;
  overflow: hidden; /* Hide overflow content */
  font-size: 14px; /* Adjust font size */
}
</style>
