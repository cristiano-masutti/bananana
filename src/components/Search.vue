<template>
  <div class="container">
    <div>
      <input v-model="chatInput" @focus="onFocus" @focusout="onFocusOut" type="text" class="input" placeholder="Type your message...">
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
      isCloseBtnActive: false
    };
  },
  mounted() {
    console.log('Component mounted.');
    this.getResponse();
  },
  methods: {
    async getResponse() {
      console.log('Getting response from server.');
      const path = 'http://127.0.0.1:5000/shark';
      try {
        const response = await axios.get(path);
        console.log(response.data);
        this.msg = response.data;
      } catch (error) {
        console.log("Error:", error);
      }
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
    }
  }
};
</script>

<style>
.container {
  position: relative;
  padding: 20px 50px;
}

.close-btn {
  position: absolute;
  top: 27px;
  right: 80px;
  font-size: 35px;
  cursor: pointer;
  color: #fff;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.close-btn.active {
  opacity: 1;
  animation: animate 0.5s linear;
}

.input {
  width: 85%;
  border: 1px solid #D9D9D9;
  background: transparent;
  padding: 15px 30px;
  border-radius: 50px;
  outline: none;
  font-size: 18px;
  color: #fff;
  letter-spacing: 1px;
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
