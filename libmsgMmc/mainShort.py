def woood(lingua,tasta):
    dicta={
        'enMY':{
            'presys':'This chatbot is UNDER CONSTRUCTING\n——————————\n',
            'con':'Create New Conversation',
            'cof':'～～～～～～～～～～\nConversation Closed\n(Key word to start a new conv.)',
            'refeson':'This chatbot is UNDER CONSTRUCTING\n——————————\nRefreshing database...',
            'refesfin':'Refreshing Finished !\n～～～～～～～～～～\n',
            'rekeswd':'～～～～～～～～～～\nGive me a word or a number',
            'bye':'See you next time! Bye!\n(Conversation Closed !)',
            'rgsWarn':"The keyword that you selected doesn't Exist or Expired\n～～～～～～～～～～\n",
            'whatsnow':"Try /whats_now ",
            'analitempo':'abratio => dtempo,utempo,cokas,cokey,targe\natren => dtempo,utempo,leve,cokas,cokey',
            'analiWarn':"Fill in all the spaces",
            'band':'～～～～～～～～～～\n',
            'spitpre':'--- PREV MSG ---\n',
            'spitpost':'\n--- NEXT MSG ---',
            'emptylist':'Sorry, try fill in other blank before request list\n',
        },
        'hanT':{
            'presys':'本聊天機器人仍處於早期開發階段\n——————————\n',
            'con':'建立新的對話',
            'cof':'～～～～～～～～～～\n對話結束\n（輸入任意文字開始新的對話）',
            'refeson':'本聊天機器人仍處於早期開發階段\n——————————\n更新資料庫',
            'refesfin':'更新完畢！！\n～～～～～～～～～～\n',
            'rekeswd':'～～～～～～～～～～\n給我一段 文字 或 數字',
            'bye':'後會有期！再見～\n（對話結束）',
            'rgsWarn':"你打算選取的關鍵字似乎不存在或過期了\n～～～～～～～～～～\n",
            'whatsnow':"試試看 /whats_now ",
            'analitempo':'abratio => dtempo,utempo,cokas,cokey,targe\natren => dtempo,utempo,leve,cokas,cokey',
            'analiWarn':"請把所有空格填滿",
            'band':'～～～～～～～～～～\n',
            'spitpre':'～文接上文～\n',
            'spitpost':'\n～文接下文～',
            'emptylist':'抱歉，請在索取項目列表前\n先嘗試填寫其他空格\n',
        },
    }
    return dicta.get(lingua,{}).get(tasta,'')
