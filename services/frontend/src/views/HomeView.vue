<template>
  <section class="d-flex align-items-center" >
    <div class="container">
      <div class="row">
        <div class="col-lg-5 d-flex flex-column justify-content-center">
          <h1 style="font-size: 3.5rem"><strong>Better Solutions For Your Business</strong></h1>
          <h5>Train your model with no knowledge of coding needed.</h5>
          <div class="d-flex justify-content-lg-start mt-3">
            <button class="btn rounded-pill px-3 py-2 text-white" style="background-color: #47b2e4; font-size: 20px;"><strong>Get Started</strong></button>
          </div>
        </div>
        <HeroImage />
      </div>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import HeroImage from '@/components/HeroImage.vue'

export default defineComponent({
  name: 'HomeView',
  components: {
    HeroImage
  },
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>