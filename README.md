# Android-sandbox
A Android Sandbox
## build
- copy `.env.example` to `.env`
    - edit `.env`
- `docker-compose up -d`
- set up backend superuser
    - `docker-compose exec backend python manage.py createsuperuser`
        - if u want to use this account as user please create a user object in admin/user/userdetail/
- set `/etc/modules-load.d/redroid.conf` in docker host
    ```
    ashmem_linux
    binder_linux
    binfmt_misc
    ```
    - reboot
- if u r running in pve make sure adding `cpu: host` to your vm conf (`/etc/pve/qemu-server/<vmid>.conf`)
## project structure
- backend
    - app (django app)
- frontend
    - nginx docker
        - `/api/` reverse proxy to backend  django
        - auto build vue.js project
    - vue.js project
        - all frontend 
        - compute with `/api/`
- worker

## Dev & debuging
- frontend 
    - cd to the folder
    - `npm install`
    - `npm run dev`
- worker & backend 
    - set the .env `DEBUG=True`
