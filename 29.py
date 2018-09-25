criticalTickets = ticket_persistence.find_opened_only_critical_tickets(region_persistence.find_region_id('Hungary'), True)

	with criticalTickets:
        for criticalTicket in criticalTickets:
        actualTicketEntryId = criticalTicket['ticketEntryId']

        try:
            team = self.__get_team_by_ticket_entry_id(collector, actualTicketEntryId)
        except Exception:
            mainLogger.log("Skipping " + str(ticket['lesaKey']) + " as no primary worker found")
            continue

		statusDocument.add_rush_ticket(team, criticalTicket['lesaKey'])

    statusDocument.set_create_date(get_now_date())
