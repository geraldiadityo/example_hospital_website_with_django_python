$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-pengaduan").modal("show");
            },
            success:function(data){
                $("#modal-pengaduan .modal-content").html(data.html_form);
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
                    alert('action data success!');
                    $("#table-pengaduan tbody").html(data.html_pengaduan_list);
                    $("#modal-pengaduan").modal("hide");
                }
                else{
                    $("#modal-pengaduan .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $("#table-pengaduan tbody").on("click",".js-pengaduan-view",loadForm);
    $("#table-pengaduan tbody").on("click",".js-pengaduan-delete",loadForm);
    $("#modal-pengaduan").on("submit",".js-pengaduan-delete-form",saveForm);
});