import random
script = open("script.txt","r").readlines()
scripts = ['local _env = function() local _s = "PROTECTED" local num = 0.429847553 num+=9398762.9287900398727768393284777726789/288937466.438772375 end','local _kam = "This sucks" local num = 023883282391284274723642367472823842.929483274645242564273429329273462374328487 num+= 9424204282094608438932899488903204.04923493204923483756326634625463463274/49294384732643743495.329943854752384539534959432887*03928427473264288437756257483274+929348238432746645.23943824739329403284824732743 local _enws = {"йцуккеннгншкзпкуххзвзащвылвьфыьвыфбчбьсывьсыюсыбсыьятимсчмырлсыовиыВИЦВЛЦЛДУГЦШКЦУКЩШЦЙГКЦРЩЦРВЫТомтмвтымвтмьллоргтгорр","ウクライナ軍によって保護されていますウクライナ軍によって保護されていますウクライナ軍によって保護されています"}','local function func()local _end = {0.4123243234242392388238428483294328773258344732832, 923497399238432.3949234204924023942384923493289348385, 020403294329483249482.450232342343242394329493249329432848329858238778327} local num = 0 for i,v in ipairs(_end) do num += v end end', 'local _p = "ыраышрашщуцвлщуовлцузвцулзащвуоаоцуоашщуцгкшгщуцкг83409кг34гк9345743853098583285809340586368586023453685375368056342650834кн3кщауоадыжлмоваратвмымлчюявмлрдыаыолоущашуцавыдоауцлшгзфажоцушагцжщау9цг0к7349к43" local num = 8294283429348724623747265627482942348327436247284923402847324234.42943248234732562743284294324832735634738492402349348373*0324932847336537453489320549328534753426537829534543.5032945837367839228573453467825934053498752356324578953025345']
obs = ""
for line in script:
    obs += random.choice(scripts)
    obs += " "
    obs += line
    obs += " "
    obs += random.choice(scripts)
    obs += " "
obs.replace("\n","")
print(script)
print(obs)