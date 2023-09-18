<template>
    <footer class="bg-dark text-center text-white">
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
            © 2023 Copyright:
            <a class="text-white" href="random url">NoCodeTrainer.com</a>
        </div>
    </footer>
</template>
    
<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Footer'
});
</script>

<style>
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 999;
    width: 100%;
    margin-top: 10px;
}
</style>