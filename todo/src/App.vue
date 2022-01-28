<template>
  <div class="page">
    <div class="container">
      <div class="header">
        <h3>Daily Todo App</h3>
        <button @click="addNew = !addNew">Add Task</button>
      </div>

      <List :show='addNew'/>
    </div>
  </div>
</template>

<script>
import List from './List.vue';
import {ref} from 'vue'
export default {
  components: { List },
  name: "App",
  setup(){
    const addNew = ref(false)
    console.log(addNew.value)
    return {
      addNew
    }
  }
};
</script>

<style>
* {
  font-family: Arial, Helvetica, sans-serif;
  padding: 0;
  margin: 0;
  color: #fff;
}

body{
  background: #11101a;
}

.page{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.container {
  height: calc(100vh - 250px);
  width: calc(100vh - 250px);
  box-shadow:  0 0 10px #0f0f0f;
  border-radius: 10px;
  overflow: hidden;
  background-image: linear-gradient(180deg, #353a50, #000);
}

.header {
  background-image: linear-gradient(120deg, #ff9138, #8049ff);
  color: #fff;
  padding: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
button{
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  outline: 0;
  border: 0;
  background: #0d0e1d;
}

input {
  padding: 8px 10px;
  font-size: 16px;
  outline: 0;
  border: 1px solid black;
  border-radius: 4px;
  background: #0d0e1d;
}
</style>
