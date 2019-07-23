<h1>Documentation</h1>
<h2>1-)What's This&How to work?</h2>
<pre>  This module finds cosine similarity of two sentences, paragraphs, documents etc... You can find similarity of the sentences paragraphs, documents with vsm module. Vsm module clears text from special charecters and converts the sentences into vectors. After that finds angle between two vectors. Similarity and angle are inversely proportional. In the other words,if cosine of the angle close 1, the sentences are similar. It finds similarity with formul that shown in Figure-1</pre>
<img src="https://raw.githubusercontent.com/alihakimtaskiran/NLP/master/Cosine%20Similarity/formula.png">
<center><pre>                                                 Figure-1</pre></center>
<h2>2.)System Requirements</h2>
<ul>
  <li>Python 3</li>
  <li>It runs on both 32-bit and 64-bit</li>
</ul>
<h2>Installation</h2>

<font size="7"><b><pre>  You can run the module including into working directory. 
You can also install it into python3. After the installation, you can run the module without including into working directory.</pre></b></font>
Follow this steps for install the module(optional)
<h3>·Linux Installation</h3>
<ol>
  <li>Open the terminal. After that</li>
  <li><code>git clone https://github.com/alihakimtaskiran/NLP.git</code></li>
  <li><code>cd "NLP/Cosine Similarity"</code></li>
  <li>sudo cp vsm.py /usr/lib/python3.6/</li>
 </ol>
 <br/>
<p>You can use the module in python3 just one lines of code:<code>import vsm</code></p>
