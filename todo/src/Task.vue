<template>
  <div class="task">
    <input type="checkbox" v-model="checked" @change="update($event)" />
    <p class="label">{{ task.description }}</p>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
export default {
  name: "Task",
  props: ["task"],
  setup(props) {
    const checked = ref("");
    if (props.task.status === "Todo") checked.value = false;
    else checked.value = true;

    const update = (e) => {
      const val = e.target.checked;
      console.log(val);
      axios
        .put(
          "http://127.0.0.1:8000/tasks/" + props.task.id + "/",
          {
            description: props.task.description,
            status: val ? "Done" : "Todo",
          },
          {
            auth: {
              username: "debjit",
              password: "1234",
            },
          }
        )
        .then(() => {
          window.location.reload();
        });
    };

    return {
      update,
      checked,
    };
  },
};
</script>

<style scoped>
.task {
  display: flex;
  align-items: center;
  padding: 16px;
  margin: 0 16px;
  cursor: pointer;
  border-radius: 6px;
}
.task:nth-child(even) {
  background: #3b4152;
}
input{
  cursor: pointer;
}
.label {
  margin: 0 0 0 16px;
  text-overflow: ellipsis;
  overflow: hidden;
  width: 80%;
  font-weight: 600;
  font-size: 18px;
}
</style>