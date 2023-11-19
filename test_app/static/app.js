new Vue({
    el: '#ui',
    data: {
        posts: []
    },
    methods: {
        uploadImage: function () {
            const vm = this;
            const fileInput = this.$refs.fileInput;
            const reader = new FileReader();
            const description = this.description;
        
            reader.onload = function (e) {
                const base64Image = e.target.result;
        
                axios.post('/add_image', { img_code: base64Image, description: description })
                    .then(function (response) {
                        console.log(response.data);
        
                        const newPost = {
                            id: response.data.id,
                            img_code: base64Image,
                            description: response.data.description,
                        };
        
                        vm.posts.push(newPost);
        
                        vm.description = '';
                        fileInput.value = '';
                    })
                    .catch(function (error) {
                        console.error(error);
                        alert('Ошибка при загрузке изображения. ' + (error.response ? error.response.data : ''));
                    });
            };
        
            reader.readAsDataURL(fileInput.files[0]);
        },
        
        

        listImages: function () {
            const vm = this;
            axios.get('/list_images')
                .then(function (response) {
                    console.log(response.data);
        
                    response.data.forEach(post => {
                        if (post.img_code) {
                            const base64Data = post.img_code.split(",")[1];
                            post.img_code = `data:image/;base64,${base64Data}`;
                        }
                    });
        
                    vm.posts = response.data;
                })
                .catch(function (error) {
                    console.error(error);
                    alert('Ошибка при загрузке изображения');                });
        },
    
        deleteImage: function (id) {
            const vm = this;
            axios.post('/delete_image', { id: id })
                .then(function (response) {
                    console.log(response.data);
                    vm.listImages();
                })
                .catch(function (error) {
                    console.error(error);
                });
        }
    },
    mounted() {
        this.listImages();
    }
    
})
