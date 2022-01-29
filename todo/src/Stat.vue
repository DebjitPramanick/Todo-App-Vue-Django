<template>
    <div class="stats">
        <div class="card">
            <span class="title">Productivity</span>
            {{ tasks.length ? (getCompleteTasks(tasks).length/tasks.length*100).toFixed(0) : 0}}%
        </div>
        <div class="card">
            <span class="title">Date</span>
            {{getDate()}}
        </div>
    </div>
</template>

<script>
import {getDate, getCompleteTasks} from "./utils"
    export default {
        name: "Stat",
        props: ["tasks"],
        setup(){

            const h = 3.455
            h.toFixed(2)

            return{
                getDate,
                getCompleteTasks
            }
        }
    }
</script>

<style scoped>
.stats{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px;
    column-gap: 16px;
}
.card{
    flex-basis: 50%;
    background-image: linear-gradient(120deg, #ff9138, #8049ff);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    border-radius: 10px;
    height: 80px;
    color: #fff;
    font-size: 28px;
    position: relative;
}

.title{
    position: absolute;
    font-size: 14px;
    top: 10px;
    left: 10px;
    font-weight: 400;
}
</style>