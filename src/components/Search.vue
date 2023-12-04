<template>
  <div class="container">
    <div style="width: 100%;">
      <input v-model="chatInput" @keyup.enter="sendRequest" @focus="onFocus" @focusout="onFocusOut" type="text" class="input" placeholder="Type your message...">
    </div>
    <div class="close-btn" @click="clearInput" :class="{ active: isCloseBtnActive }">&times;</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SharkVue',
  data() {
    return {
      msg: "",
      chatInput: "",
      isCloseBtnActive: false,
      previosQuery: "",
    };
  },
  props: {
    oldQuery: String,
  },
  watch: { 
    oldQuery: 'sendRequestOnQueryChange',
  },
  methods: {
    sendRequestOnQueryChange() {
      this.chatInput = this.oldQuery;
      if (this.oldQuery) {
        this.sendRequestOld();
      }
    },
    sendRequest() {
      console.log('Sending request to server.');
      const path = `http://127.0.0.1:5000/${this.chatInput}`;
      
      axios.get(path)
        .then(response => {
          // Handle the response from the server
          console.log(response.data);
          const data = response.data;
          this.$emit('search', this.chatInput, data);
        })
        .catch(error => {
          // Handle any errors that occurred during the request
          console.error('Error:', error);
        });
        this.previosQuery = "";
    },
    sendRequestOld() {
      this.previosQuery = this.oldQuery;
      const path = `http://127.0.0.1:5000/${this.previosQuery}`;

      axios.get(path)
        .then(response => {
          // Handle the response from the server
          console.log(response.data);
          const data = response.data;
          this.$emit('search', this.chatInput, data);
        })
        .catch(error => {
          // Handle any errors that occurred during the request
          console.error('Error:', error);
        });
    },
    onFocus() {
      this.isCloseBtnActive = true;
    },
    onFocusOut() {
      this.isCloseBtnActive = false;
      this.chatInput = "";
    },
    clearInput() {
      this.chatInput = "";
    },
  }
};
</script>

<style>
.container {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center; 
  position: relative;
  padding: 10px 50px;
}

.input {
  width: 100%;
  border: .5px solid #D9D9D9;
  background: transparent;
  padding: 15px 30px;
  border-radius: 50px;
  outline: none;
  font-size: 18px;
  color: #fff;
  letter-spacing: 1px;
}

.close-btn {
  font-size: 35px;
  cursor: pointer;
  color: #fff;
  opacity: 0;
  transition: opacity 0.5s ease;
  margin-left: 10px; /* Add some spacing between input and button */
}

.close-btn.active {
  opacity: 1;
  animation: animate 0.5s linear;
}

::-webkit-input-placeholder {
  color: #fff;
  letter-spacing: 2px;
  text-transform: uppercase;
}

::-moz-placeholder {
  color: #fff;
}

:-ms-input-placeholder {
  color: #fff;
}
</style>
