$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-departement").modal("show");
            },
            success:function(data){
                $("#modal-departement .modal-content").html(data.html_form);
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
                if(data.form_is_valid){
                    alert("data sender success");
                    $("#table-departement tbody").html(data.html_departement_list);
                    $("#modal-departement").modal("hide");
                }
                else{
                    $("#modal-departement .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-departement-add").click(loadForm);
    $("#modal-departement").on("submit",".js-departement-add-form",saveForm);
    $("#table-departement tbody").on("click",".js-departement-edit",loadForm);
    $("#modal-departement").on("submit",".js-departement-edit-form",saveForm);
    $("#table-departement tbody").on("click",".js-departement-delete",loadForm);
    $("#modal-departement").on("submit",".js-departement-delete-form",saveForm);
});