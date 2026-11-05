/* Оболочка в кэше: открыли с домашнего экрана в подземном паркинге — страница есть.
   HTML и каталог берём сетью вперёд: иначе клиент увидит вчерашний список дисков.
   Картинки и прочую статику — кэшем вперёд, они версионируются через ?v=. */
var V = "wz-en-v3";
var SHELL = ["./", "./catalog.json?v=2"];

self.addEventListener("install", function(e){
  e.waitUntil(
    caches.open(V).then(function(c){
      /* по одному, а не addAll: addAll кладёт всё или ничего, и один промах
         оставлял бы оболочку вообще без кэша — молча */
      return Promise.all(SHELL.map(function(u){ return c.add(u).catch(function(){}); }));
    }).then(function(){ return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function(e){
  e.waitUntil(
    caches.keys()
      .then(function(keys){
        return Promise.all(keys.map(function(k){ return k === V ? null : caches.delete(k); }));
      })
      .then(function(){ return self.clients.claim(); })
  );
});

function store(req, res){
  var copy = res.clone();
  caches.open(V).then(function(c){ c.put(req, copy); });
  return res;
}

self.addEventListener("fetch", function(e){
  var req = e.request;
  if(req.method !== "GET") return;
  var url = new URL(req.url);
  if(url.origin !== location.origin) return;     /* карта и шрифты идут мимо воркера */

  var fresh = req.mode === "navigate"
           || url.pathname.indexOf(".json") > -1
           || url.pathname.indexOf(".html") > -1;

  if(fresh){
    e.respondWith(
      fetch(req).then(function(r){ return store(req, r); })
                .catch(function(){
                  return caches.match(req).then(function(m){ return m || caches.match("./"); });
                })
    );
  } else {
    e.respondWith(
      caches.match(req).then(function(m){
        return m || fetch(req).then(function(r){ return store(req, r); });
      })
    );
  }
});
