<template>
  <div class="add">
    <input
      type="text"
      placeholder="Enter task description"
      :value="description.value"
      @change="onChange($event)"
    />
    <button @click="addTask"><p>+</p></button>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
export default {
  name: "AddTask",
  setup() {
    const description = ref("");

    const onChange = (e) => {
        console.log(e.target.value)
        description.value = e.target.value
    }

    const addTask = () => {
      axios.post(
        "http://127.0.0.1:8000/tasks/",
        { description: description.value },
        {
          auth: {
            username: "debjit",
            password: "1234",
          },
        }
      ).then(() => {
          window.location.reload()
      })
    };
    return {
      description,
      addTask,
      onChange
    };
  },
};
</script>

<style scoped>
.add {
  display: flex;
  align-items: center;
  border-radius: 4px;
  overflow: hidden;
  background: #0d0e1d88;
}

.add input {
  padding:0;
  font-size: 16px;
  width: 0;
  outline: 0;
  border: 0;
  border-radius: 4px;
  margin-right: 0;
  background: transparent;
  transition: 0.5s;
}

button:hover .add input{
  width: calc(100% - 60px);
  padding: 9px 10px;
  margin-right: 16px;
}

button {
  border-radius: 4px;
  width: 40px;
  padding: 9px 10px;
  background-image: linear-gradient(45deg, #8063e052, #103e9260);
  outline: 0;
  border: 0;
  color: #fff;
  cursor: pointer;
}
button p{
  transform: scale(2);
}
</style>