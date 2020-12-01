<template>
<div class="callback">
  Please wait until you're redirected...
</div>

</template>

<script>
import { setIdToken, setAccessToken } from '../auth0-service';

    export default {
        name: 'Callback',
        mounted: function() {
            console.log("I am into callback");
            setAccessToken();
            setIdToken();
            window.location.href = '/';
        },
    };
</script>
