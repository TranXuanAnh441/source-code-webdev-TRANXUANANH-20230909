<template>
  <section>
    <h1>Models</h1>
    <p>Create new model <router-link :to="{ name: 'Create Model' }">here</router-link></p>
    <hr />
    <div class="active-cyan-3 active-cyan-4 input-group w-auto mb-2">
      <input class="form-control col-lg-5" type="text" placeholder="Search by description" aria-label="Search" v-model="search_str">
      <button class="btn btn-primary" @click="search()">Search</button>
    </div>
    <br />
    <h5 v-if="!models">No models</h5>
    <div v-else class="models row row-cols-1 row-cols-md-5">
      <div v-for="m in models" :key="m.id">
        <ModelListItem :m="m" />
      </div>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
import ModelListItem from '@/components/ModelListItem.vue';

export default defineComponent({
  name: 'Models',
  components: {
    ModelListItem,
  },
  data() {
    return {
      search_str: '',
    }
  },
  created: function () {
    return this.$store.dispatch('getModels');
  },
  computed: {
    ...mapGetters({ models: 'stateModels' }),
  },
  methods: {
    ...mapActions(['searchModels']),
    async search() {
      await this.searchModels(this.search_str);
    }
  }
});
</script>