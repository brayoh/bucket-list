"use strict";
(function() {
    var BucketList = {
        init: function() {
            this.bucketListModal = document.querySelector('#addBucketListModal');
            this.activityModal = document.querySelector('#addActivityModal');
            this.bucketListInputs = [].slice.call(document.querySelectorAll('#addBucketListModal .modal-input')) // mozilla fix for document.querySelectorAll
            this.activityModalInputs = [].slice.call(document.querySelectorAll('#addActivityModal .modal-input')) // mozilla fix for document.querySelectorAll
            this.modalForm = document.querySelector(".modal form");
            this.addEventListeners();
            var header = document.getElementsByTagName("header")[0];
            if (header) {
                var height = window.innerHeight;
                header.style.height = height + 'px';
            }
        },
        addEventListeners: function() {
            var self = this; // set self to this due to context when calling show modal
            var floating_blist_btn = document.querySelector('#add-bucket-list') || undefined;
            var floating_activity_btn = document.querySelector('#add-activity') || undefined;
            if (floating_blist_btn) {
                floating_blist_btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    $(self.bucketListModal).modal('show');
                });
            } else if(floating_activity_btn){
                floating_activity_btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    $(self.activityModal).modal('show');
                });
            }

            $(this.activityModal).on('hidden.bs.modal', function () {
                $('div.status').addClass('hidden');
            })

        },
        updateBucketListInputs(blist_id, blist_name, blist_description) {
            // update inputs for the bucket list modal
            var self = this;
            this.bucketListInputs.forEach(function(input) {
                switch (input.type) {
                    case "text":
                        input.value = blist_name;
                        break;
                    case "textarea":
                        input.value = blist_description
                        break;
                    case "hidden":
                        input.value = blist_id
                        break;
                    default:
                        input.value = "";
                        break;
                }
            });
        },
        updateActivityInputs(activity_id, activity_name) {
            // update inputs for the activity modal
            var self = this;
            this.activityModalInputs.forEach(function(input) {
                switch (input.type) {
                    case "text":
                        input.value = activity_name;
                        break;
                    case "hidden":
                        input.value = activity_id
                        break;
                }
            });
        },
        showModal(id, name, description, modal_type, activity_status) {
            if (modal_type === 'add-bucket-list') {
                var form = document.querySelector('#bucketlist-form');

                // takes name and description of bucketList and appends to modal inputs
                this.updateBucketListInputs(id, name, description);
                $(this.bucketListModal).modal('show');

                // change the form method to get
                form.setAttribute("method","get");
            } else if (modal_type === 'add-activity') {
                var form = document.querySelector('#activity-form');
                $('div.status').removeClass('hidden');
                var checkbox = document.querySelector('#activity_toggle');
                console.log(activity_status);
                if (activity_status === 'done') {
                    checkbox.setAttribute("checked","checked");
                }
                else{
                    checkbox.removeAttribute("checked");
                }
                this.updateActivityInputs(id, name);
                $(this.activityModal).modal('show');

                // change the form method to get
                form.setAttribute("method","get");
                console.log(form);
            }
        }
    };
    BucketList.init();
    window.BucketList = BucketList;
}())
