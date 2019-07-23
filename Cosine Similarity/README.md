<h1>Documentation</h1>
<h2>What's This&How to work?</h2>
<pre>  This module finds cosine similarity of two sentences, paragraphs etc... You can find similarity of the sentences paragraphs with vsm module. Vsm module clears text from special charecters and converts the text into vectors. After that finds angle between two vectors. Similarity and angle are inversely proportional. In the other words,if cosine of the angle close 1, the sentences are similar. It finds similarity with formul that shown in Figure-1</pre>
<img src="https://raw.githubusercontent.com/alihakimtaskiran/NLP/master/Cosine%20Similarity/formula.png">
<center><pre>                                                 Figure-1</pre></center>
<h2>2.)System Requirements</h2>
<ul>
  <li>Python 3</li>
  <li>Numpy</li>
  <li>It runs on both 32-bit and 64-bit</li>
</ul>
<h2>Installation</h2>

<font size="7"><b><pre>  You can run the module including into working directory. 
You can also install it into python3. After the installation, you can run the module without including into working directory.</pre></b></font>
Follow this steps for install the module(optional)
<h3>·Installation Steps for Linux</h3>
<ol>
  <li>Open the terminal. After that</li>
  <li><code>git clone https://github.com/alihakimtaskiran/NLP.git</code></li>
  <li><code>cd "NLP/Cosine Similarity"</code></li>
  <li><code>sudo cp vsm.py /usr/lib/python3.6/</code></li>
  <li>If you haven't installed numpy, install the numpy with <code>pip3 install numpy</code></li>
 </ol>
<p>Finally, you can use the module in python3 just one lines of code:<code>import vsm</code></p>
<h2>Functions of Module?</h2>
<pre>  Here you are a tree for the commands</pre>
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
  <li><code>vsm.np</code><pre><b> type:module</b> You can the use numpy module as <code>vsm.np</code> without import into main file.</pre></li>
  <li><code>vsm.wordlist</code><pre><b> type:list</b> Imported words are in the <code>vsm.wordlist</code></pre></li>
  <li><code>vsm.import_contents(string)</code><pre><b> type:function</b> This function is very important. It imports strings for computing similarity. The module can't work correctly without importing strings. You have to import all sentences with <code>vsm.import_contents(sentence)</code> before other calculations. The function clears text from special charecters, then it appends all words into <code>vsm.wordlist</code>. </pre></li>
  <li><code>vsm.func</code><pre><b>type:class</b> This class has useful functions such as <code>is_in()</code>, <code>doc2vec()</code> and <code>cossim()</code></pre>
  <ul>
    <li><code>vsm.func.is_in(string)</code><pre><b>type:function</b> This function searches a word in <code>vsm.wordlist</code></pre>. Then returns True or False.</li>
    <li><code>vsm.func.doc2vec(string)</code><pre><b>type:function</b> It converts sentence or paragraph into vector. It returns one dimensional numpy array. The vector has frequency of words in the text. <b>Caution:<b> You have to import the text with <code>vsm.import_contents()</code> before using. Otherwise you get error.</pre></li>
    <li><code>vsm.func.cossim(np.array,np.array)</code><pre><b>type:function</b> The function gets two vector as input. It returns cosine similarity of two vectors. dimensions of vectors must be equal. If you import all texts at the before vector conversion, you don't get error.</pre></li>
  </ul>
  </li>
<ul>
