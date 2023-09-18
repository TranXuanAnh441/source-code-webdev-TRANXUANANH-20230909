<template>
    <div class="card rounded-6 mb-3">
        <img src="https://previews.123rf.com/images/dtosh/dtosh1811/dtosh181100072/114656557-database-icon-simple-flat-logo-of-database-04-vector.jpg"
            class="card-img-top">
        <div class="card-body">
            <p class="card-text">
                <strong>created at:</strong> {{ dataset.created_at }}<br/>
                <strong>Title:</strong> {{ dataset.title }}
            </p>
        </div>
        <div class="card-footer bg-transparent"><router-link
                :to="{ name: 'Dataset', params: { id: dataset.id } }">Details</router-link></div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'DatasetListItem',
  props: {
    dataset: Object
  }
});
</script>