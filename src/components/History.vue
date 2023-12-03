<template>
    <div style="background-color: #D9D9D9; margin-top: 10px; margin-right: 50px; margin-bottom: 30px; height: 70vh; overflow-y: auto;">
      <h1 style="margin-left: 10px">History</h1>
      <!-- Use v-for to iterate over each element in the query array -->
      <div v-for="(item, index) in query" :key="index" style="margin-left: 10px">
        <div @click="sendItemToParent(item)" style="margin-left: 10px; cursor: pointer;">
            {{ item }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'SharkVue',
    data() {
      return {
        msg: '',
      };
    },
    props: {
      query: Array,
    },
    methods: {
        sendItemToParent(item) {
            this.$emit('item-clicked', item);
        },
    },
  };
  </script>
  