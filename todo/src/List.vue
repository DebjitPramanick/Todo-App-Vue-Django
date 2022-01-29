<template>
  <div class="list">
    <Stat :tasks="tasks"/>
    <SearchBar @search="handleSeacrh" />

    <div class="tasks">
      <h3>Incomplete Tasks({{ getInCompleteTasks(tasks).length }})</h3>
      <Task
        v-for="task in getInCompleteTasks(tasks)"
        :key="task.id"
        :task="task"
      />

      <h3>Complete Tasks ({{ getCompleteTasks(tasks).length }})</h3>
      <Task
        v-for="task in getCompleteTasks(tasks)"
        :key="task.id"
        :task="task"
      />
    </div>
  </div>
</template>

<script>
import Task from "./Task.vue";
import axios from "axios";
import { ref, onBeforeMount } from "vue";
import { getInCompleteTasks, getCompleteTasks } from "./utils.js";
import SearchBar from "./SearchBar.vue";
import Stat from './Stat.vue';

export default {
  name: "List",
  components: { Task, SearchBar, Stat },
  setup() {
    const tasks = ref([]);
    const tasksStore = ref([]);

    onBeforeMount(() => {
      axios
        .get("http://127.0.0.1:8000/tasks/", {
          auth: {
            username: "debjit",
            password: "1234",
          },
        })
        .then((res) => {
          tasks.value = res.data;
          tasksStore.value = res.data;
        });
    });

    const handleSeacrh = (val) => {
      let res = [...tasksStore.value];
      res = res.filter((n) => {
        return n.description.toLowerCase().includes(val.toLowerCase());
      });
      tasks.value = res;
    };

    return {
      tasks,
      getCompleteTasks,
      getInCompleteTasks,
      handleSeacrh,
    };
  },
};
</script>

<style scoped>
.list{
  height: calc(100% - 84px);
}
.tasks {
  height: calc(100% - 210px);
  overflow-y: scroll;
}

@media (max-width: 576px) {
  
}

h3 {
  margin: 20px 16px 10px 16px;
  color: #929292;
}

::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  border-radius: 10px;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #2c2b2b; 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #575658; 
}
</style>