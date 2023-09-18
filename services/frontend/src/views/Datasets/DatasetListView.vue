<template>
  <section>
    <h1>Datasets</h1>
    <p>Create your own dataset <router-link :to="{ name: 'Create Dataset' }">here</router-link></p>
    <hr />
    <div class="active-cyan-3 active-cyan-4 input-group w-auto mb-2">
      <input class="form-control col-lg-5" type="text" placeholder="Search by title" aria-label="Search" v-model="search_str">
      <button v-on:click="now()" class="btn btn-primary" >Search</button>
    </div>
    <br />
    <h5 v-if="!datasets">No datasets</h5>
    <div v-else class="datasets row row-cols-1 row-cols-md-5">
      <div v-for="dataset in datasets" :key="dataset.id">
        <DatasetListItem :dataset="dataset" />
      </div>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
import DatasetListItem from '../../components/DatasetListItem.vue';

export default defineComponent({
  name: 'DatasetListView',
  data() {
    return {
      search_str: '',
    };
  },
  components: {
    DatasetListItem
  },
  methods: {
    ...mapActions(['searchDatasets']),
    async now() {
      console.log(this.search_str);
      await this.searchDatasets(this.search_str);
    }
  },
  created: function () {
    return this.$store.dispatch('getDatasets');
  },
  computed: {
    ...mapGetters({ datasets: 'stateDatasets' }),
  },
});
</script>