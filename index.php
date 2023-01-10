<?php

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot';
$conn = mysqli_connect($servidor,$usuario,$senha,$banco);

if(!$conn){

} else{


}

?>

<?php

$menu1 = "Olá bem vindo, sou seu atendente vitual da proex\n vamos começar seu atendimento, escolha uma das opções\n
*1* *Eventos de extensão*\n
*2* *Bolsas de extensão*\n
*3* *PIBEX*\n
*4* *cadastro de evento*\n
*5* *atendimento presencial*\n";


$menuOp1 = "Opção eventos de extensão";

$menuOp2 = "Opção Bolsas de extensão";

$menuOp3 = "Opção Pibex";

$menuOp4 = "Opção cadastro de evento";

$menuOp5 = "Opção atendimento presencial";


$data = date('d/m/Y');
?>

<?php 

$msg = $_GET['msg'];
$telefone = $_GET['telefone'];

 $sql = "SELECT * FROM usuario WHERE telefone = '$telefone'";
    $query = mysqli_query($conn, $sql);
    $total = mysqli_num_rows($query);

 if ($total > 0){

    echo "numero encontrado";
 }else {

$sql = "INSERT INTO usuario (telefone, status) VALUE ('telefone', '1')";
$query = mysqli_query($conn, $sql);

if(!$query){


}else {

echo $menu1;


}
 }


?>

<?php

$sql = "SELECT * FROM usuario WHERE telefone = '$telefone'";
$query = mysqli_query($conn, $sql);

//while($rows_usuarios = mysqli_fetch_array($query)){
//    $status = $rows_usuarios['status'];
//}
$resposta = $_GET['msg'];

if($resposta == '1'){

    echo $menuOp1;
    $respostaBot = $menuOp1;
}
elseif($resposta == '2'){
    
    echo $menuOp2;
    $respostaBot = $menuOp2;
}
elseif($resposta == '3'){
    
    echo $menuOp3;
    $respostaBot = $menuOp3;
}
elseif($resposta == '4'){
    
    echo $menuOp4;
    $respostaBot = $menuOp4;
}
elseif($resposta == '5'){
    
    echo $menuOp5;
    $respostaBot = $menuOp5;
}
?>

<?php

$sql = "INSERT INTO historico (telefone, cliente, bot, data) VALUE ('$telefone', '$msg', '$respostaBot', '$data')";
$query = mysqli_query($conn, $sql);

?>