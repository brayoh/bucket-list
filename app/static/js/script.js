"use strict";
(function(){
    var BucketList = {
        init: function(){
            this.modal = document.querySelector('#addBucketListModal');
            this.inputs = [].slice.call(document.querySelectorAll('.modal-input')) // mozilla fix for document.querySelectorAll
            this.modalForm = document.querySelector(".modal form");
            this.addEventListeners();
            var header = document.getElementsByTagName("header")[0];
            if (header) {
                var height = window.innerHeight;
                header.style.height = height + 'px';
            }
        },
        addEventListeners: function(){
            var floating_btn = document.querySelector('#action-button');
            var self = this;
            floating_btn.addEventListener('click', function(e) {
                e.preventDefault();
                $(self.modal).modal('show');
            });
        },
        updateInputs(blist_id, blist_name, blist_description){
            var self = this;
            this.inputs.forEach(function(input){
                switch (input.type) {
                    case "text":
                        input.value = blist_name;
                        break;
                    case "textarea":
                        input.value = blist_description
                        break;
                    default:
                        // do nothing
                        break;
                }
            });
        },
        showModal(blist_id, blist_name, blist_description){
            // takes name and description of bucketList and appends to modal inputs
            this.updateInputs(blist_id, blist_name, blist_description);
            $(this.modal).modal('show');
            return false
        }
    };
    BucketList.init();
    window.BucketList = BucketList;
}())
