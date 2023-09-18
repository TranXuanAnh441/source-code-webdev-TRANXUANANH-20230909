import axios from 'axios';

const state = {
  datasets: null,
  dataset: null
};

const getters = {
  stateDatasets: state => state.datasets,
  stateDataset: state => state.dataset,
};

const actions = {
  async createDataset({}, dataset) {
    console.log(dataset);
    await axios.post('api/datasets', dataset);
  },
  async getDatasets({
    commit
  }) {
    let {
      data
    } = await axios.get('api/datasets');
    console.log(data);
    commit('setDatasets', data.datasets);
  },
  async searchDatasets({
    commit
  }, search_str) {
    let {
      data
    } = await axios.get('api/datasets', {
      params: {
        'search': search_str,
      }
    });
    console.log(data);
    commit('setDatasets', data.datasets);
  },
  async viewDataset({
    commit
  }, id) {
    let {
      data
    } = await axios.get(`api/datasets/${id}`);
    console.log(data);
    commit('setDataset', data);
  },
  async updateDataset({}, dataset) {
    await axios.patch(`api/datasets/${dataset.id}`, dataset.form);
  },
  async deleteDataset({}, id) {
    await axios.delete(`api/datasets/${id}`);
  },
  async logOutDataset({
    commit
  }) {
    commit('setDataset', null);
    commit('setDatasets', null);
  },
  async uploadFile({}, file) {
    console.log(file);
    await axios.post('api/datasetFile/upload', file, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  },
  async downloadFile({}, file_id) {
    console.log(file_id);
    axios.get('api/datasetFile/download', {
      params: {
        datasetFileId: file_id
      }
    }, {
      headers: {
        'Response-Type': 'arraybuffer'
      }
    }).then(function (response) {
      let blob = new Blob([response.data], {
        type: 'text/csv'
      })
      let link = document.createElement('a')
      link.href = window.URL.createObjectURL(blob)
      link.download = 'file.csv'
      link.click()
    })
  },
};

const mutations = {
  setDatasets(state, datasets) {
    state.datasets = datasets;
  },
  setDataset(state, dataset) {
    state.dataset = dataset;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};