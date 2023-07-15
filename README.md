<h1 align="center">
    <tt>>basic-django-prototype</tt>
</h1>
<h3 align="left">
    Descripción
</h3>
<p>
    Proyecto de django enfocado en el aprendizaje de los recursos basicos que ofrece el Framework al usuario para realizar distintas acciones en el desarrollo web de manera practica y sencilla. Se recrea una aplicación web que gestiona los usuarios de una empresa, registrando empleados, editandolos, eliminandolos y consultandolos, haciendo lo mismo para los departamentos dentro de la misma empresa. Lo creado se enfoca principalmente en lo funcional y no en lo grafico. En el mismo se lleva a practica los siguientes conceptos:
    <ul>
        <li>
            <p>Patrones de diseño en Django (Modelo-Vista-Template, manejo de links con reverse-lazy y especificaciónes, division de procesos).</p>
        </li>
        <li>
            <p>Uso de base de datos con Django (PostgreSQL). Unicamente haciendo uso del pionero ORM del framework.</p>
        </li>
        <li>
            <p>Uso de vistas genericas de Django (ListView, DetailView, DeleteView, UpdateView, CreateView).</p>
        </li>
        <li>
            <p>Uso del administrador ofrecido de django y personalización del mismo.</p>
        </li>
        <li>
            <p>Conceptos varios (paginación, etc.).</p>
        </li>
    </ul>
</p>
<hr/>
<h3 aling = "left"> Uso </h3>
<p>
    <ol>
        <li>
             Clonar el repositorio: git clone https://github.com/kristianrpo/basic-django-prototype.git
        </li>
        <li>
             Ir a la carpeta: cd basic-django-prototipe
        </li>
        <li>
             Instalar entorno virtual:  py -m venv nombre_del_entorno_virutal
        </li>
        <li>
             Instalar entorno virtual:  py -m venv venv
        </li>
        <li>
             Activar entorno virtual:  source venv/bin/activate
        </li>
        <li>
             Instalar dependencias:  pip install django, pip install psycopg2, pip install unipath y pip install os
        </li>
        <li>
             Crear base de datos en PostgreSQL: CREATE DATABASE nombre_bd;
        </li>
        <li>
             Crear usuario de base de datos: CREATE USER “nombre_usuario”;;
        </li>
        <li>
             Crear usuario de base de datos: CREATE USER “nombre_usuario”;
        </li>
        <li>
             Ingresar a la base de datos: \c nombre_base_datos;
        </li>
        <li>
             Crear contraseña al usuario: ALTER USER “usuario_creado” WITH PASSWORD 'una_contraseña';
        </li>
         <li>
             Establecer permisos en la base de datos: ALTER DATABASE nombrebd OWNER TO usuario_creado;
        </li>
        <li>
             En el archivo "local.py" en la configuración del proyecto, establecer los datos correspondientes para hacer la conexión con la base de datos.
        </li>
        <li>
             Migrar la base de datos: python manage.py makemigrations; y luego: python manage.py migrate
        </li>
        <li>
            Crear un super usuario: python manage.py createsuperuser
        </li>
        <li>
             Iniciar proyecto: python manage.py runserver
        </li>
    </ol>
</p>

<hr/>
<h3 align="left">
    Capturas del proyecto
<br/>
</h3>
<div align="center">
    <img src='https://i.imgur.com/Nh4UlHo.png' height='280px'/>
    <img src='https://i.imgur.com/dxJBmRd.png' height='280px'/>
    <img src='https://i.imgur.com/w1kAfN1.png' height='280px'/>
    <img src='https://i.imgur.com/ghDdMeV.png' height='280px'/>
    <img src='https://i.imgur.com/XIscoiz.png' height='280px'/>
    <img src='https://i.imgur.com/78Xw3r3.png' height='280px'/>
</div>
<hr/>
<h3 align="left">
    Autor
<br/>
</h3>
<p>
    Kristian Restrepo Osorio
</p>
