<template>
    <div class="col-lg-7 hero-img">
        <img src="../assets/img/hero-img.png" class="img-fluid bounce">
    </div>
</template>

<style>
img-fluid {
    height: auto;
}

@keyframes bounce {
    0% {
        transform: translateY(0);
    }

    30% {
        transform: translateY(-10px);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0);
    }
}

.bounce {
    animation: bounce 2s;
    animation-timing-function: ease;
    animation-iteration-count: infinite;
}
</style>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'HeroImage',
});
</script>