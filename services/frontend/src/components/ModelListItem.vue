<template>
    <div class="card rounded-6 mb-3">
        <img src="https://is3-ssl.mzstatic.com/image/thumb/Purple122/v4/7f/cf/64/7fcf6459-755a-1ea8-9757-de830f8de2cd/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg"
            class="card-img-top">
        <div class="card-body">
            <p class="card-text">
                <strong>created at:</strong> {{ m.created_at }}<br/>
                <strong>Description:</strong> {{ m.description }}
            </p>
        </div>
        <div class="card-footer bg-transparent"><router-link
                :to="{ name: 'Model', params: { id: m.id } }">Details</router-link></div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'ModelListItem',
    props: {
        m: Object
    }
});
</script>