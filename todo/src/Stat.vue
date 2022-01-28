<template>
    <div class="stats">
        <div class="card">
            16%
        </div>
        <div class="card">
            {{getDate()}}
        </div>
    </div>
</template>

<script>
import {getDate} from "./utils"
    export default {
        name: "Stat",
        setup(){
            return{
                getDate
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
}
</style>