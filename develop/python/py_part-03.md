# **Web Scraping Fundamentos**  

* Investigar sobre HTML  

* Investigar sobre la etiqueta `<script>` y para que sirve.  

* Investigar que son los metadatos y como incluirlos dentro de un documento html.   

* Investigar cual es la etiqueca html que permite  incluir un sitio web dentro de otro.  

14 Web Scraping Tools:  
https://www.scraperapi.com/blog/the-10-best-web-scraping-tools/

## **XPATH**

Es un lenguaje que permite moverse entre nodos, hasta llegar al nodo donde esta la información que se desea extraer.  
XML path language  
**`//div/span//h1[@class='title'][1]`**

Un nodo es lo mismo que la etiqueta y su contenido.  


### **Tipos de nodos**  


URL practicar: 

* http://toscrape.com/  
* https://www.upwork.com/  
* https://www.workana.com/es  

documentación:

http://plasmasturm.org/log/xpath101/

$x('//h1/text()').map(x => x.wholeText)
['Web Scraping Sandbox']

#### predicados

$x('/html/body/div')
[div.container]0: div.containerlength: 1[[Prototype]]: Array(0)
$x('/html/body/div/div[1]')
[div.row.header-box]
$x('/html/body/div/div[last()]')
[div.row]

#### atributos

$x('//span[@class="text"]/text()').map(x => x.wholeText)
(10) ['“The world as we have created it is a process of o…cannot be changed without changing our thinking.”', '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', '“There are only two ways to live your life. One is… The other is as though everything is a miracle.”', '“The person, be it gentleman or lady, who has not …ure in a good novel, must be intolerably stupid.”', "“Imperfection is beauty, madness is genius and it'…be absolutely ridiculous than absolutely boring.”", '“Try not to become a man of success. Rather become a man of value.”', '“It is better to be hated for what you are than to be loved for what you are not.”', "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", '“A day without sunshine is like, you know, night.”']

$x('//span[@class!="text"]')
(11) [span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.sh-red]  


$x('html/body/div/div[position()>1]')
[div.row]

$x('//span[@class="text" and @class="tag-item"]')
[]

$x('//span[@class="text" or @class="tag-item"]')
(20) [span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.text, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item, span.tag-item]  


$x('//span[not(@class)]')
(11) [span, span, span, span, span, span, span, span, span, span, span]

$x('html/*')
(2) [head, body]


$x('//*')
(152) [html, head, meta, title, link, link, script, body, div.container, div.row.header-box, div.col-md-8, h1, a, div.col-md-4, p, a, div.row, div.col-md-8, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, div.quote, span.text, span, small.author, a, div.tags, meta.keywords, a.tag, a.tag, a.tag, a.tag, …]

$x('html/body//span/@*')
(32) [class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, class, itemprop, aria-hidden, class, class, class, class, class, class, class, class, class, class, class]

$x('//span[@class="text" and @itemprop="text"]/node()')
(10) [text, text, text, text, text, text, text, text, text, text]

$x('//span[@class="text" and @itemprop="text"]/*')
[]

#### **In-text search en Xpath**   

