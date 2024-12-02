$flag = Read-Host "Quieres crear un venv? Escribe SI en caso de tenerlo, cualquier otro input no creara el entorno"
if ($flag -eq "SI"){
    Write-Host "Creando venv..."
    python -m venv venv
}


.\venv\Scripts\Activate.ps1
pip install -r requirements.txt


