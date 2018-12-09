class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s=len(s)
        len_p=len(p)
        result=False
        if p=='*':
            result=True
        elif len_p>len_s:
            result=False
        else:
            start=0
            p_list=p.split('*')

            for subs in p_list:
                counter=0
                sub_list = subs.split("?")
                for subchars in sub_list:
                    if counter==0 and start >0:
                        index = s.find(subchars, start)
                    else:
                        index = s.find(subchars, start, start+len(subchars))
                    counter=counter+1

                    if index==-1:
                        result=False
                        break
                    else:
                        start = index + len(subchars)+1
                if result==False:
                    break

            if subs=='' and result!=False:
                result=True
            elif start>len(s):
                result=True
            else:
                result=False
                return result
