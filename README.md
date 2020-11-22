<h1>Documentation</h1>
<h2>1-)What's This&How to work?</h2>
<p>  This module finds cosine similarity of two sentences, paragraphs etc... You can find similarity of the sentences paragraphs with vsm module. Vsm module clears text from special charecters and converts the text into vectors. After that finds angle between two vectors. Similarity and angle are inversely proportional. In the other words,if cosine of the angle close 1, the sentences are similar. It finds similarity with formula that shown in Figure-1</p>
<img src="https://raw.githubusercontent.com/alihakimtaskiran/NLP/master/formula.png">
<center><pre>                                                 Figure-1</pre></center>
<h2>2-)System Requirements</h2>
<ul>
  <li>Python 3</li>
  <li>Numpy</li>
  <li>It runs on both 32-bit and 64-bit</li>
</ul>
<h2>3-)Installation</h2>

<font size="7"><b><p>  You can run the module including into working directory. 
You can also install it into python3. After the installation, you can run the module without including into working directory.</p></b></font>
Follow this steps for install the module(optional)
<h3>·Installation Steps for Linux</h3>
<ol>
  <li>Open the terminal. After that</li>
  <li><code>git clone https://github.com/alihakimtaskiran/NLP.git</code></li>
  <li><code>cd "VSM"</code></li>
  <li><code>sudo cp vsm.py /usr/lib/python3.6/</code></li>
  <li>If you haven't installed numpy, install the numpy with <code>pip3 install numpy</code></li>
 </ol>
<p>Finally, you can use the module in python3 just one lines of code:<code>import vsm</code></p>
<h2>4-)Functions of Module?</h2>
<p>  Here you are a tree for the commands</p>
<pre>
<code>
vsm---|
      |---np
      |---wordlist
      |---import_contents()
      |---func---|
                 |---is_in()
                 |---doc2vec()
                 |---cossim()
  
</code>
</pre>
<ul>
  <li><code>vsm.np</code><p><b> type:module</b> You can the use numpy module as <code>vsm.np</code> without import into main file.</p></li>
  <li><code>vsm.wordlist</code><p><b> type:list</b> Imported words are in the <code>vsm.wordlist</code></p></li>
  <li><code>vsm.import_contents(string,integer)</code><p><b> type:function</b> This function is very important. It imports strings for computing similarity. The module can't work correctly without importing strings. You have to import all sentences with <code>vsm.import_contents(sentence,0 or 1)</code> before other calculations. The function clears text from special charecters, then it appends all words into <code>vsm.wordlist</code>. After release v1.2 it supports Chinese. If you want to import English, Espanol, Turkish, Germany, French, Russian, Korean(this languages has space between words), second parameter is 0.<code>vsm.import_contents(text,0)</code>.You can also use <code>vsm.import_contents(text)</code>. Because default second parameter is 0. If you want to import text in Chinese(there is no space between Chinese words), the second parameter is 1.<code>vsm.import_contents(text,1)</code>.</p></li>
  <li><code>vsm.func</code><p><b>type:class</b> This class has useful functions such as <code>is_in()</code>, <code>doc2vec()</code> and <code>cossim()</code></p>
  <ul>
    <li><code>vsm.func.is_in(string)</code><p><b>type:function</b> This function searches a word in <code>vsm.wordlist</code>. Then returns True or False.</p></li>
    <li><code>vsm.func.doc2vec(string)</code><p><b>type:function</b> It converts sentence or paragraph into vector. It returns one dimensional numpy array. The vector has frequency of words in the text. <b>Caution:</b> You have to import the text with <code>vsm.import_contents()</code> before using. Otherwise you get error.</p></li>
    <li><code>vsm.func.cossim(np.array,np.array)</code><p> <b>type:function</b> The function gets two vector as input. It returns cosine similarity of two vectors. Vectors must be in same dimensions. If you import all texts at the before vector conversion, you don't get error.</p></li>
  </ul>
  </li>
<ul>
