import { createStore } from "vuex";
import VuexPersist from 'vuex-persist';

import users from './modules/users';
import datasets from './modules/datasets';
import models from './modules/models';
import trainings from './modules/trainings';

const vuexLocalStorage = new VuexPersist({
  key: 'key', 
  storage: window.localStorage,
});

export default createStore({
  name: 'store',
  modules: {
    users,
    datasets,
    models,
    trainings
  },
  plugins: [vuexLocalStorage.plugin],
});