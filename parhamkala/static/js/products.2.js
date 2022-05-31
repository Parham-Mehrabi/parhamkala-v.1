function del_conf(a){
    var c = confirm("are you sure you want to delete this product?")
    if (c){
        window.location.href = './delete/'+a
    }
}
