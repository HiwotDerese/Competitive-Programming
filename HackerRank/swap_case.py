def swap_case(s):
    m=""
    for i in range(len(s)):
        if s[i].islower():
            m += s[i].upper()
        elif s[i].isupper():
            m += s[i].lower() 
        else:
            m += s[i]  
    return(m)

# if __name__ == '__main__':