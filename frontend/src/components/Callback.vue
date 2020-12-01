<template>
<div class="Callback">
  Please wait until you're redirected...
</div>

</template>

<script>
import { setIdToken, setAccessToken } from '../auth0-service';

    export default {
        name: 'Callback',
        mounted: function() {
            setAccessToken();
            setIdToken();
            window.location.href = '/page0';
        },
    };
</script>
