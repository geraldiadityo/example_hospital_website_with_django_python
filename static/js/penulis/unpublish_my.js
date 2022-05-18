$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-unpublish").modal("show");
            },
            success:function(data){
                $("#modal-unpublish .modal-content").html(data.html_form);
            },
        });
    };
    
    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url:form.attr("action"),
            type:form.attr("method"),
            data:form.serialize(),
            dataType:"JSON",
            success:function(data){
                if (data.form_is_valid){
                    alert("publish arcticle success!");
                    $("#table-unpublish tbody").html(data.html_unpublish_list);
                    $("#modal-unpublish").modal("hide");
                }
                else{
                    $("#moda-unpublish .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $("#table-unpublish tbody").on("click",".js-published-artikel",loadForm);
    $("#modal-unpublish").on("submit",".js-published-artikel-form",saveForm);
});