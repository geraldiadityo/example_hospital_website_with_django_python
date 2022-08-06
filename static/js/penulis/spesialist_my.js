$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-spesialist").modal("show");
            },
            success:function(data){
                $("#modal-spesialist .modal-content").html(data.html_form);
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
                    alert("data success sender!");
                    $("#table-spesialist tbody").html(data.html_spesialist_list);
                    $("#modal-spesialist").modal("hide");
                }
                else{
                    $("#modal-spesialist .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $("#table-spesialist tbody").on("click",".js-spesialist-delete",loadForm);
    $("#modal-spesialist").on("submit",".js-spesialist-delete-form",saveForm);

});