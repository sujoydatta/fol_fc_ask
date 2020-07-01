def fol_fc_ask(KB, alpha):
    """Inefficient forward chaining for first-order logic. [Fig. 9.3]
    KB is a FolKB and alpha must be an atomic sentence."""
    KB= fol_fc_infer(KB);
    for r in KB.clauses:
        ps, q = parse_definite_clause(standardize_variables(r));
        log=1;
        dd={};
        if len(ps)==0:
            ans=unify(expr(alpha), q, {});
            if ans != None:
                return ans;
            else:
                continue;
        if len(ps)==1:
            continue;
        for p in ps:
            flag=0;
            for pprm in KB.clauses:
                theta=unify(p, pprm, dd);
                if theta != None:
                    log=log*1;
                    flag=1;
                    dd=theta;
            if flag==0:
                log=log*0;
                break;
        if log==1:
            e=expr(subst(dd,q))
            if e not in KB.clauses:
                KB.tell(e);
    return False;
 
                        

def fol_fc_infer(KB):
    new=['0'];
    while True:
        '''print new'''
        l=len(new)
        if l==0:
            return KB
        new = [];
        for r in KB.clauses:
            '''print r'''
            ps, q = parse_definite_clause(standardize_variables(r));
            if len(ps)>1:
                continue;
            for p in ps:
                '''print p'''
                for pprm in KB.clauses:
                    theta=unify(p, pprm, {});
                    '''print theta'''
                    if theta != None:
                        '''print theta'''
                        qprm=subst(theta, q);
                        '''print qprm'''
                        if ((qprm not in new) and (qprm not in KB.clauses)):
                            new.append(qprm);
                        '''phi=unify(qprm, theta, {});
                        if phi != None:
                            return phi;
                            print theta
                            return phi;'''
                        

        for nn in new:
            '''print nn'''
            KB.tell(expr(nn));
    return KB;
