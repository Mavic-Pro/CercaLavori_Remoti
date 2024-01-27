# Import necessary libraries
import argparse
import streamlit as st
from search_engines.engines import search_engines_dict
from search_engines.multiple_search_engines import MultipleSearchEngines, AllSearchEngines
from search_engines import config

def main():
    st.title("Search Engine Query Web App")

    # Collect user input using Streamlit widgets
    user_query = st.text_input("What job are you looking for?")
    search_engines = st.selectbox("Select Search Engine(s)", list(search_engines_dict.keys()), index=0)
    output_format = st.selectbox("Select Output Format", ["html", "csv", "json"], index=0)
    output_filename = st.text_input("Enter Output Filename", config.OUTPUT_DIR + 'output')
    num_pages = st.number_input("Enter Number of Pages", value=config.SEARCH_ENGINE_RESULTS_PAGES, min_value=1)
    filter_results = st.text_input("Filter Results [url, title, text, host]")
    ignore_duplicates = st.checkbox("Ignore Duplicates")
    proxy = st.text_input("Use Proxy (protocol://ip:port)", config.PROXY)

    # Perform search when the user clicks the button
    if st.button("Search"):
        timeout = config.TIMEOUT + (10 * bool(proxy))
        engines = [e.strip() for e in search_engines.lower().split(',') if e.strip() in search_engines_dict or e.strip() == 'all']

        if not engines:
            st.error('Please choose a search engine: ' + ', '.join(search_engines_dict))
        else:
            if 'all' in engines:
                engine = AllSearchEngines(proxy, timeout)
            elif len(engines) > 1:
                engine = MultipleSearchEngines(engines, proxy, timeout)
            else:
                engine = search_engines_dict[engines[0]](proxy, timeout)

            engine.ignore_duplicate_urls = ignore_duplicates
            if filter_results:
                engine.set_search_operator(filter_results)

            st.info("Searching... Please wait.")
            # Replace the ellipsis (...) with your full search query
            engine.search(user_query + " AND site:20tab.com/careers OR site:linkedin.com/company/3beesrl/jobs/ OR site:5w155.ch/careers OR site:blhack.it/jobs OR site:extendi.it/careers OR site:advigator.com/careers OR site:linkedin.com/company/aimaidhelp/jobs OR site:linkedin.com/company/aicof/jobs/ OR site:linkedin.com/company/aikospace/jobs OR site:aiven.io/careers OR site:bitbull.it/team/ OR site:bitrock.it/join-us OR site:bobsled.co/company/ OR site:linkedin.com/company/bonusxitalia/jobs OR site:brave.com/careers/ OR site:linkedin.com/company/breadcrumbsio/jobs/ OR site:buzzoole.com/page/jobs OR site:linkedin.com/company/calton-io/jobs OR site:canonical.com/careers OR site:linkedin.com/company/capbase/jobs/ OR site:careers.casavo.com/ OR site:claranetitalia.recruitee.com/l/it OR site:coders51.typeform.com/to/BpB9pe OR site:codiceplastico.com/ OR site:collabora.com/careers.html OR site:linkedin.com/company/getcoverflex/jobs OR site:linkedin.com/company/daito-solutions/about/jobs OR site:letsdeel.com/careers OR site:digitalscience.pinpointhq.com/#js-careers-jobs-block OR site:docebo.com/company/careers/ OR site:linkedin.com/company/donq OR site:doubleloop.io/jobs.html OR site:duckduckgo.com/hiring OR site:elastic.co/about/careers/ OR site:eleva.it/team/ OR site:elfo.net/en/work-with-us/ OR site:apply.workable.com/empatica/ OR site:enhancers.it/culture/ OR site:help.ernesto.it/contatti/ OR site:etiqa-srl.breezy.hr/ OR site:it.everli.com/it/lavora-con-noi OR site:faberbee.com/en/job.html OR site:corporate.faceit.com/working-at-faceit/ OR site:fastcode.it/lavora-con-noi/ OR site:fastloop.it/careers/ OR site:linkedin.com/company/fiscozen/ OR site:fourtheorem.com/careers OR site:careers.frontiersin.org/ OR site:linkedin.com/company/gamindo/jobs/ OR site:linkedin.com/company/geodatalab-srls/jobs/ OR site:career.getir.com/ OR site:giantswarm.io/careers#open-positions OR site:docplanner.com/career OR site:about.gitlab.com/jobs/ OR site:sorint.com/en/careers/ OR site:hakuna.jobs.personio.de/ OR site:hasura.io/careers/ OR site:careers.heritageholdings.co/ OR site:linkedin.com/company/heveloon-ltd OR site:linkedin.com/company/hlpy/jobs/ OR site:hopper.com/careers OR site:careers.hotjar.com/ OR site:linkedin.com/company/hyland-software/ OR site:ignt.com/careers OR site:linkedin.com/company/imola-informatica/jobs OR site:linkedin.com/company/in4it/jobs/ OR site:careers.infinitaslearning.com/o/software-engineer OR site:axelerant.it/carriere/ OR site:linkedin.com/company/innovi-/ OR site:withintent.com/careers OR site:jobs.intergiro.com/ OR site:linkedin.com/company/intribetrend/jobs OR site:investsuite.com/jobs OR site:linkedin.com/company/iubenda/jobs OR site:jagaad.com/careers OR site:linkedin.com/company/jethr/jobs/ OR site:juni.co/careers OR site:kiratech.it/en/work-with-us OR site:linkedin.com/company/klondike/jobs/ OR site:linkedin.com/company/kpi6/jobs OR site:careers.lastminute.com/ OR site:linkedin.com/school/learnn-srl/jobs OR site:lightcode.net/ OR site:linkedin.com/company/lualtek/jobs OR site:linkedin.com/company/macaiit/jobs/ OR site:labs.madisoft.it/entra-nel-team/ OR site:linkedin.com/company/manageddesigns/jobs OR site:medicilio.it/careers OR site:meritocracy.is/it/seltishub OR site:metacareers.com/jobs?roles[0]=full-time&offices[0]=Remote%2C%20Italy OR site:corporate.miaburton.com/en/jobs/ OR site:careers.microsoft.com/ OR site:miinto-group.com/jobs/ OR site:mindedsecurity.com/jobs/ OR site:namastudio.it/pages/careers OR site:nearform.com/careers/ OR site:nebulab.com/careers OR site:netlify.com/careers/ OR site:newesis.com/career OR site:nibol.notion.site/Careers-at-Nibol-3fab744eabd34c479abf44089cd9f299 OR site:linkedin.com/company/notonlydesk/jobs OR site:linkedin.com/company/ofcourseme-official/jobs OR site:linkedin.com/company/onlytech-industries/jobs OR site:outfitterygmbh.teamtailor.com/ OR site:linkedin.com/company/pack-mentoring/jobs OR site:linkedin.com/company/ai-patch/jobs/ OR site:angel.co/company/pexels/jobs OR site:pinv.it/lavora-con-noi/ OR site:linkedin.com/company/polaris-engineering-spa/jobs/ OR site:popguide.me/careers.php OR site:it.prima.jobs/?lang=it-it OR site:primer.io/careers/ OR site:linkedin.com/company/qapla'-srl/jobs OR site:qredo.com/careers OR site:linkedin.com/company/radicalstorage/jobs/ OR site:jobs.r-control.de/game-developer-jobs/ OR site:careers-redhat.icims.com/jobs/search?ss=1&searchLocation=13270--Remote OR site:refactory-project.com/join-the-team/ OR site:remotamente.it/en/job/ OR site:boards.greenhouse.io/remotecom OR site:searchmetrics.com/company-and-careers/ OR site:corporate.shopfully.com/it/lavora-con-noi/ OR site:shopify.com/careers OR site:linkedin.com/company/sighup/jobs/ OR site:linkedin.com/company/smace/jobs OR site:sorint.com/en/careers/ OR site:sorintoss.io/contact/ OR site:notion.so/getclayton/Work-at-Clayton-98fa028f39b44129989d44a02bbbd374 OR site:careers.sparkfabrik.com/ OR site:careers.spreaker.com/ OR site:linkedin.com/company/sqlitecloud/jobs/ OR site:careers.fcagroup.com/ OR site:linkedin.com/company/storeis/jobs OR site:apply.workable.com/storyteq/ OR site:superlayer-1634135852323.freshteam.com/jobs OR site:jobs.suse.com/ OR site:switcho.it/jobs OR site:linkedin.com/company/thei/jobs OR site:tlmpartners.com/being-a-monster/ OR site:treatwell.com/openings/ OR site:linkedin.com/company/unguess/jobs OR site:userbot.ai/it/jobs-opportunities/ OR site:veed.io/careers OR site:linkedin.com/company/vlk-studio OR site:careers.vmware.com/main/jobs?stretch=10&stretchUnit=MILES&lat=&lng=&location=Italy&woe=12&keywords=&brand=&categories=&locations=&page=1&tags=Yes OR site:linkedin.com/company/voipvoice/jobs OR site:wave.com/en/careers/ OR site:linkedin.com/company/wavelop/jobs OR site:wikimediafoundation.org/about/jobs/ OR site:wuerth-phoenix.com/posizioni-aperte OR site:zapier.com/jobs/ OR site:jobs.zendesk.com/us/en OR site:linkedin.com/company/zextras/jobs/ OR site:zupit.it/careers.html")

            engine.output(output_format, output_filename)
            st.success(f"Search complete. Results saved to {output_filename}.{output_format}")

if __name__ == '__main__':
    main()
