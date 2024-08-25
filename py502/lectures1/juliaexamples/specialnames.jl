# Function and variable names can use Unicode characters
# Almost any character from any language is allowed
# It may be painful to enter special characters
# In the Julia REPL, Latex commands can be used to type in characters:
# δ is obtained by \delta<tab>, and this can be pasted if your editor allows
# Here is an example using Chinese characters and Greek letters

function 大学(γ)
   α=1
   β=1
   δ=α+β+γ
   return δ
end

println(大学(2))

# Note: The characters may not show correctly in a browser, should be OK in downloaded file

